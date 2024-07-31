from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import datetime
from .forms import DoctorForm
from .models import *
from django.contrib.auth import authenticate, login, logout
import pandas as pd
import numpy as np
from lightgbm import LGBMClassifier
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import FetalDetailForm
import matplotlib.pyplot as plt
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import joblib
import pandas as pd
import numpy as np
import shap
import io
import base64
import urllib
import matplotlib.pyplot as plt
from lime.lime_tabular import LimeTabularExplainer
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set_style('darkgrid')
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.model_selection import train_test_split
from django.http import HttpResponse
import io
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMClassifier
from django.views.decorators.csrf import csrf_protect
from lime.lime_tabular import LimeTabularExplainer
from django.http import HttpResponseBadRequest
import shap
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
import pandas as pd
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from .models import Admin_Fetal_Health_CSV, Patient, Search_Data, Doctor
from .forms import FetalDetailForm
from lightgbm import LGBMClassifier
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
# views start here

def Home(request):
    return render(request,'carousel.html')

def Admin_Home(request):
    dis = Search_Data.objects.all()
    pat = Patient.objects.all()
    doc = Doctor.objects.all()
    feed = Feedback.objects.all()

    d = {'dis':dis.count(),'pat':pat.count(),'doc':doc.count(),'feed':feed.count()}
    return render(request,'admin_home.html',d)
@login_required(login_url="login")
def assign_status(request,pid):
    doctor = Doctor.objects.get(id=pid)
    if doctor.status == 1:
        doctor.status = 2
        messages.success(request, 'Selected doctor are successfully withdraw his approval.')
    else:
        doctor.status = 1
        messages.success(request, 'Selected doctor are successfully approved.')
    doctor.save()
    return redirect('view_doctor')

@login_required(login_url="login")
def User_Home(request):
    return render(request,'patient_home.html')

@login_required(login_url="login")
def Doctor_Home(request):
    return render(request,'doctor_home.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')


def Gallery(request):
    return render(request,'gallery.html')


def Login_User(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        sign = ""
        if user:
            try:
                sign = Patient.objects.get(user=user)
            except:
                pass
            if sign:
                login(request, user)
                error = "pat1"
            else:
                pure=False
                try:
                    pure = Doctor.objects.get(status=1,user=user)
                except:
                    pass
                if pure:
                    login(request, user)
                    error = "pat2"
                else:
                    login(request, user)
                    error="notmember"
        else:
            error="not"
    d = {'error': error}
    return render(request, 'login.html', d)

def Login_admin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user.is_staff:
            login(request, user)
            error="pat"
        else:
            error="not"
    d = {'error': error}
    return render(request, 'admin_login.html', d)

def Signup_User(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['pwd']
        d = request.POST['dob']
        con = request.POST['contact']
        add = request.POST['add']
        type = request.POST['type']
        im = request.FILES['image']
        dat = datetime.date.today()
        user = User.objects.create_user(email=e, username=u, password=p, first_name=f,last_name=l)
        if type == "Patient":
            Patient.objects.create(user=user,contact=con,address=add,image=im,dob=d)
        else:
            Doctor.objects.create(dob=d,image=im,user=user,contact=con,address=add,status=2)
        error = "create"
    d = {'error':error}
    return render(request,'register.html',d)

def Logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url="login")
def Change_Password(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    if not request.user.is_staff:
        try:
            sign = Patient.objects.get(user=user)
            if sign:
                error = "pat"
        except:
            sign = Doctor.objects.get(user=user)
    terror = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            terror = "yes"
        else:
            terror = "not"
    d = {'error':error,'terror':terror,'data':sign}
    return render(request,'change_password.html',d)
@login_required(login_url="login")
def add_doctor(request,pid=None):
    doctor = None
    if pid:
        doctor = Doctor.objects.get(id=pid)
    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance = doctor)
        if form.is_valid():
            new_doc = form.save()
            new_doc.status = 1
            if not pid:
                user = User.objects.create_user(password=request.POST['password'], username=request.POST['username'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                new_doc.user = user
            new_doc.save()
            return redirect('view_doctor')
    d = {"doctor": doctor}
    return render(request, 'add_doctor.html', d)
@login_required(login_url="login")
def view_search_pat(request):
    doc = None
    try:
        doc = Doctor.objects.get(user=request.user)
        data = Search_Data.objects.filter(patient__address__icontains=doc.address).order_by('-id')
    except:
        try:
            doc = Patient.objects.get(user=request.user)
            data = Search_Data.objects.filter(patient=doc).order_by('-id')
        except:
            data = Search_Data.objects.all().order_by('-id')
    return render(request,'view_search_pat.html',{'data':data})

@login_required(login_url="login")
def delete_doctor(request,pid):
    doc = Doctor.objects.get(id=pid)
    doc.delete()
    return redirect('view_doctor')

@login_required(login_url="login")
def delete_feedback(request,pid):
    doc = Feedback.objects.get(id=pid)
    doc.delete()
    return redirect('view_feedback')

@login_required(login_url="login")
def delete_patient(request,pid):
    doc = Patient.objects.get(id=pid)
    doc.delete()
    return redirect('view_patient')

@login_required(login_url="login")
def delete_searched(request,pid):
    doc = Search_Data.objects.get(id=pid)
    doc.delete()
    return redirect('view_search_pat')

@login_required(login_url="login")
def View_Doctor(request):
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)

@login_required(login_url="login")
def View_Patient(request):
    patient = Patient.objects.all()
    d = {'patient':patient}
    return render(request,'view_patient.html',d)

@login_required(login_url="login")
def View_Feedback(request):
    dis = Feedback.objects.all()
    d = {'dis':dis}
    return render(request,'view_feedback.html',d)

@login_required(login_url="login")
def View_My_Detail(request):
    terror = ""
    user = User.objects.get(id=request.user.id)
    error = ""
    try:
        sign = Patient.objects.get(user=user)
        error = "pat"
    except:
        sign = Doctor.objects.get(user=user)
    d = {'error': error,'pro':sign}
    return render(request,'profile_doctor.html',d)

@login_required(login_url="login")
def Edit_Doctor(request,pid):
    doc = Doctor.objects.get(id=pid)
    error = ""
    # type = Type.objects.all()
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        add = request.POST['add']
        cat = request.POST['type']
        try:
            im = request.FILES['image']
            doc.image=im
            doc.save()
        except:
            pass
        dat = datetime.date.today()
        doc.user.first_name = f
        doc.user.last_name = l
        doc.user.email = e
        doc.contact = con
        doc.category = cat
        doc.address = add
        doc.user.save()
        doc.save()
        error = "create"
    d = {'error':error,'doc':doc,'type':type}
    return render(request,'edit_doctor.html',d)

@login_required(login_url="login")
def Edit_My_deatail(request):
    terror = ""
    print("Hii welcome")
    user = User.objects.get(id=request.user.id)
    error = ""
    # type = Type.objects.all()
    try:
        sign = Patient.objects.get(user=user)
        error = "pat"
    except:
        sign = Doctor.objects.get(user=user)
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        add = request.POST['add']
        try:
            im = request.FILES['image']
            sign.image = im
            sign.save()
        except:
            pass
        to1 = datetime.date.today()
        sign.user.first_name = f
        sign.user.last_name = l
        sign.user.email = e
        sign.contact = con
        if error != "pat":
            cat = request.POST['type']
            sign.category = cat
            sign.save()
        sign.address = add
        sign.user.save()
        sign.save()
        terror = "create"
    d = {'error':error,'terror':terror,'doc':sign}
    return render(request,'edit_profile.html',d)

@login_required(login_url='login')
def sent_feedback(request):
    terror = None
    if request.method == "POST":
        username = request.POST['uname']
        message = request.POST['msg']
        username = User.objects.get(username=username)
        Feedback.objects.create(user=username, messages=message)
        terror = "create"
    return render(request, 'sent_feedback.html',{'terror':terror})

# Predict, displayed related views are  below;
# Load data

def predict_disease(request, pred, accuracy):
    accuracy = float(accuracy)
    context = {
        'prediction': pred,
        'accuracy': accuracy
    }
    return render(request, 'predict_disease.html', context)


# error 
def error_404(request, exception):
    return render(request, '404.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)

# Load data
# ndata = pd.read_csv('machine_learning/ndata.csv')
@login_required(login_url='login')
@csrf_exempt
def add_fetaldetail(request):
    if request.method == 'POST':
        try:
            # Parse input features from the request
            Prolongued = float(request.POST['Prolongued'])
            Percentage = float(request.POST['Percentage'])
            Accelerations = float(request.POST['Accelerations'])
            Abnormal = float(request.POST['Abnormal'])
            Severe = float(request.POST['Severe'])
            Histogram_variance = float(request.POST['Histogram_variance'])
            light_decelerations = float(request.POST['light_decelerations'])
            Histogram_min = float(request.POST['Histogram_min'])
            Uterine_contractions = float(request.POST['Uterine_contractions'])
            mean_value = float(request.POST['mean_value'])
            Histogram_mean = float(request.POST['Histogram_mean'])
            Baseline_value = float(request.POST['Baseline_value'])
            explanation_type = request.POST['explanation_type']
            
            features = np.array([
                Prolongued, Percentage, Accelerations, Abnormal, Severe, Histogram_variance,
                light_decelerations, Histogram_min, Uterine_contractions, mean_value, Histogram_mean, Baseline_value
            ]).reshape(1, -1)
            
            # Load the dataset
            ndata_path = r'C:\Users\user\Downloads\ndata.csv'
            ndata = pd.read_csv(ndata_path)
            
            # Map target variable from 1, 2, 3 to 0, 1, 2
            ndata['fetal_health'] -= 1
            
            # Separate features and target
            X = ndata.drop(columns=['fetal_health'])
            y = ndata['fetal_health']
            
            # Scale the dataset
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            
            # Apply SMOTE
            smote = SMOTE(random_state=42)
            X_resampled, y_resampled = smote.fit_resample(X_scaled, y)
            
            # Split the dataset
            X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.1, random_state=42)
            
            # Train the model
            clf = LGBMClassifier()
            clf.fit(X_train, y_train)
            
            # Predict the input features
            features_scaled = scaler.transform(features)
            prediction = clf.predict(features_scaled)
            prediction_proba = clf.predict_proba(features_scaled)
            
            explanation_html = ''
            
            # Generate LIME explanations for all classes
            if explanation_type == 'lime':
                class_names = ['Normal', 'Suspect', 'Pathological']
                explanations = []

                for class_name in class_names:
                    explainer = LimeTabularExplainer(training_data=X_train,
                                                     feature_names=X.columns.tolist(),
                                                     class_names=class_names,
                                                     discretize_continuous=True)
                    
                    exp = explainer.explain_instance(features_scaled[0], clf.predict_proba, num_features=len(X.columns), top_labels=len(class_names))
                    exp_str = exp.as_html()
                    explanations.append(exp_str)
                
                explanation_html = ''.join(explanations)
            
            # Generate SHAP explanation
            elif explanation_type == 'shap':
                try:
                    explainer = shap.Explainer(clf, X_train)
                    shap_values = explainer(features_scaled)
                    
                    shap.initjs()
                    shap_plot = shap.waterfall_plot(shap.Explanation(values=shap_values.values[0],
                                                                     base_values=shap_values.base_values[0],
                                                                     data=features_scaled[0]), max_display=12)
                    
                    buf = io.BytesIO()
                    plt.savefig(buf, format='png')
                    buf.seek(0)
                    string = base64.b64encode(buf.read())
                    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
                    explanation_html = f"<img src='{uri}'/>"
                except Exception as shap_error:
                    return render(request, 'error_page.html', {'error_message': f"SHAP explanation error: {shap_error}"})
            
            context = {
                'prediction': prediction[0],  # Map prediction back to 1, 2, 3
                'accuracy': prediction_proba.max(),
                'explanation': explanation_html
            }
            
            return render(request, 'predict_disease.html', context)
        
        except Exception as e:
            return render(request, 'error_page.html', {'error_message': str(e)})
    
    return render(request, 'add_fetaldetail.html')
