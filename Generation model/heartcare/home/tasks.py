from celery import shared_task

@shared_task
def generate_report_task(medical_report):
    llm_gen = Ollama(model="llama2",
                     system="As a Cardiac Specialist, you are tasked with generating a detailed report for a patient's condition specifically in the context of risk of developing Myocardial Infarction using only the data provided. DO NOT ASSUME ANYTHING.")
    prompt = f"""
        Create a detailed report for the following patient:

        {medical_report}
        USE ONLY THE ABOVE INFORMATION. DO NOT ASSUME ANY NEW INFORMATION
    """
    report = llm_gen(prompt)
    MedicalRecord.objects.create(record=report)