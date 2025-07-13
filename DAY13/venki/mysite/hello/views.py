from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf(request):
    # Some sample data to show in PDF
    context = {
        'title': 'Test PDF',
        'message': 'Hello! This PDF was generated from Django.'
    }

    # Load template and render it with context
    template = get_template('pdf_template.html')
    html = template.render(context)

    # Create response as PDF
    response = HttpResponse(content_type='pdf')
    response['Content-Disposition'] = 'inline; filename="test.pdf"'

    # Generate PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors while generating PDF')
    return response