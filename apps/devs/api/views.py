import time
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from apps.devs.services.pdf_service import PdfService
from apps.devs.services.mail_service import MailService
from core.messages.message_channel import MessageChannel





class DevApiViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
  
            
    @action(detail=False, methods=['get'], url_path='test')
    def invoke(self, request):
        try:
            
            MessageChannel.send(
                text=f"Invoke ejecutado: {time.time()}",
                title="CRON TEST",
            )
            
            response = {
                "message": "OK OKKKKK"
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




    @action(detail=False, methods=['get'], url_path='test_pdf')
    def invoke_pdf(self, request):
        """
            Generación de PDF de prueba.
        """
        try:
            
            ## - Generar PDF y descargarlo
            
            # pdf_service = CreatePdfService()
            # pdf_bytes = pdf_service.generate_pdf({
            #     "title": "PDF de prueba",
            #     "body": "Hola, este es un PDF generado desde Django con wkhtmltopdf.",
            # })
            # response = HttpResponse(pdf_bytes, content_type="application/pdf")
            # response["Content-Disposition"] = 'attachment; filename="prueba.pdf"'
            # return response
        
        
            ## - Guardar PDF en carpeta uploads/pdfs
            
            pdf_service = PdfService(
                template_html="pdfs/test_pdf.html"
            )

            file_path = pdf_service.save(
                filename="prueba.pdf",
                context={
                    "title": "PDF guardado",
                    "body": "Hola, este PDF se ha guardado en la carpeta uploads/pdfs.",
                }
            )
            
            response = {
                "message": "PDF generado y guardado correctamente",
                "file_path": file_path,
            }
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



    
    @action(detail=False, methods=['get'], url_path='test_email')
    def invoke_email(self, request):
        ''' Envio de correo de prueba.'''
        try:
            
            mail_service = MailService(
                subject="Correo Prueba",
                to_emails=["doriandarren1@gmail.com"],
            )
            
            mail_service.send_html_mail(
                title="Correo de prueba",
                body="Hola,\n\nEste es un correo de prueba.\n\nGracias por tu tiempo."
            )
            
            
            response = {
                "message": "OK"
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    