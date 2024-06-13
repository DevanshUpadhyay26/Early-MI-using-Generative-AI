from django.shortcuts import render
from .forms import InputForm
import torch
import langchain
from langchain_community.llms import Ollama
from pytorch_tabnet.tab_model import TabNetClassifier
from django.http import StreamingHttpResponse, JsonResponse
from langchain.callbacks.manager import CallbackManager
from langchain_community.chat_models import ChatOllama
from .models import ChatHistory, ChatSummary, MedicalRecord
import time
import json
medical_report = ''
model = TabNetClassifier()
model.load_model('./model/HeartTabNet.zip')
llm_summarise = Ollama(model='llama2', num_predict=86)
llm_chat = ChatOllama(model='llama2',
                  system = 'You are a helpful medical assistant. Keep your responses short and to the point.')
# chat_history = ''


# Create your views here.
def predict(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():

            age = form.cleaned_data['Age']
            gender = 1 if form.cleaned_data['Gender'] == 'M' else 0
            ecg = 1 if form.cleaned_data['ECG'] == 'Y' else 0
            ckmb = 1 if form.cleaned_data['CKMB'] == 'Y' else 0
            Trop_I = 1 if form.cleaned_data['Trop_I'] == 'Y' else 0
            LAD = form.cleaned_data['LAD']
            LCA = form.cleaned_data['LCA']
            RCA = form.cleaned_data['RCA']
            Systolic = form.cleaned_data['Systolic']
            Diastolic = form.cleaned_data['Diastolic']
            Chest_Pain = 1 if form.cleaned_data['Chest_Pain'] == 'Y' else 0
            Diabetic = 1 if form.cleaned_data['Diabetic'] == 'Y' else 0
            Cholestrol = form.cleaned_data['Cholestrol']
            PHF = 1 if form.cleaned_data['PHF'] == 'Y' else 0
            Add = form.cleaned_data['Add']

            data = [[age, gender, ecg, ckmb, Trop_I, LAD, LCA, RCA, Systolic, Diastolic, Chest_Pain, Diabetic, Cholestrol, PHF]]  # Modify this according to your ML model input format
            input_tensor = torch.tensor(data).to(model.device).float()
            # Use your ML model to make predictions
            prediction = model.predict(input_tensor)[0]
            pred_label = {0:'Early Risk of MI', 1: 'MI detected', 2: 'No Risk of MI'}

            #LLM REPORT
            form_dict = {'Age':age, 'Gender':gender, 'ECG':ecg, 'CKMB':ckmb, 'TROP-I':Trop_I, 'LAD':LAD,
                         'LCA':LCA, 'RCA':RCA, 'Systolic':Systolic, 'Diastolic':Diastolic, 'Chest_Pain':Chest_Pain,
                         'Diabetic':Diabetic, 'Cholestrol':Cholestrol, 'PHF':PHF, 'Additional_Information':Add}
            global medical_report
            medical_report = form_dict

            generate_report()
            #report = MedicalRecord.objects.first()
            return render(request, 'results.html', {'form': form, 'prediction': pred_label[prediction]})
    else:
        form = InputForm()
    return render(request, 'input.html', {'form': form})

def generate_report():
    llm_gen = Ollama(model="llama2",
                 system = "As a Cardiac Specialist, you are tasked with generating a detailed report for a patient's condition specifically in the context of risk of developing Myocardial Infarction using only the data provided. DO NOT ASSUME ANYTHING.")
    prompt = f"""
        Create a detailed report for the following patient:

        {medical_report}
        USE ONLY THE ABOVE INFORMATION. DO NOT ASSUME ANY NEW INFORMATION
"""
    report = llm_gen(prompt)
    print(report)
    MedicalRecord.objects.create(record=report)

def view_report(request):
    op = MedicalRecord.objects.first()
    print(op.record)
    return render(request, 'report.html', {'report':op.record})

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        print(user_input)
        # Use LLM to generate output based on user input
        generated_output = generate_output(user_input)
        generate_chat_history(user_input, generate_output)
        #print(generated_output)
        ChatHistory.objects.create(user_input=user_input, generated_output=generated_output)
    chat_history = ChatHistory.objects.all()
   # print(ChatHistory.objects.order_by('-created_at').first().user_input)
    return render(request, 'chat.html', {'chat_history': chat_history})

def generate_output(input_text):
    try:
        chat_summary = ChatSummary.objects.get(pk=1)
        chat_hist = chat_summary.history
    except Exception as e:
        error = e
        chat_hist = ''

#     prompt = f"""
#     Below is the medical report of the user:
#     {medical_report}

#     Below is the chat history so far:
#     {chat_hist}

#     Using these, answer the following user query in a short and concise manner. DO NOT ASSUME ANY INFORMATION.
#     ### User Query: {input_text}
# """
    prompt = f"""
Respond to the following user message in a clear and concise manner:
### User Message: {input_text}

You may use the following information if necessary:
### Medical Report: {medical_report}
If this information is not needed, then do not use it.

If you do not know the answer, say I don't know.
"""
    output = llm_chat.invoke(prompt)
    return output.content

def generate_chat_history(user_message, bot_message):
    chat_summary, _ = ChatSummary.objects.get_or_create(pk=1)
    prompt = f"""
    Following is the chat history so far:
    {chat_summary.history}
    
    Following are the new messages:
    ### USER: {user_message}
    ### BOT: {bot_message}

    Generate a new small summary of the whole conversation based on this.
"""
    chat_summary.history = str(llm_summarise(prompt))
    #print(chat_summary.history)
    # Save the updated chat summary
    chat_summary.save()

def delete_all_entries(request):
    ChatHistory.objects.all().delete()
    ChatSummary.objects.all().delete()
    MedicalRecord.objects.all().delete()
    return render(request, 'end.html')
