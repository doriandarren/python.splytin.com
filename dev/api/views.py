import random
import time
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ai.data.prompts import ARR_PROMPTS
from core.helpers.helper_base64 import sd_txt2img_first_image_bytes
from core.http.api_request import ApiRequest
from core.messages.message_channel import MessageChannel
from ollama_images.models import OllamaImage
from ollama_texts.models import OllamaText


class DevApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
        
    
    MODEL = "gpt-oss:latest"
    
    
    def list(self, request):
        # GET /api/v1/dev/
        
        prompt = random.choice(ARR_PROMPTS)
        
        
        ## Ollama Text
        payload_text = {
            "model": self.MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "Eres un asistente experto escritor y siempre haces historias muy buenas. Cortas y precisas."
                },
                {
                    "role": "user",
                    "content": "por favor solo di Hola"
                    ## me puedes crear una historia corta del siguiente propmpt: ${prompt}
                }
            ],
            "stream": False
        }
        
        endpoint = ApiRequest(base_url="http://192.168.1.104:11434/")
        response_text = endpoint.post("/v1/chat/completions", payload_text)
        
        ollama_text = OllamaText.objects.create(
            model=self.MODEL,
            request_prompt=prompt,
            request_payload=payload_text,
            response_payload=response_text,
        )
        
        
        
        # Ollama Image
        payload_image = {
            "request_prompt": prompt,
            "steps": 20,
            "width": 512,
            "height": 512,
            "seed": -1,
            "cfg_scale": 7,
            ##sampler_index: 'Euler a',
            "sampler_index": 'DPM++ 2M',
            "nonce": int(time.time() * 1000), ## solo para evitar caché
        }
        
        endpoint = ApiRequest(base_url="http://192.168.1.104:7860/sdapi/")
        response_image = endpoint.post("v1/txt2img", payload_image)
        
        ##print(response_image)
        
        image_bytes = sd_txt2img_first_image_bytes(response_image)
        
        ollama_image = OllamaImage.objects.create(
            ollama_text_id=ollama_text,
            request_prompt=prompt,
            request_payload=payload_image,
            response_payload=response_image,
            nonce=payload_image["nonce"],
            sampler_index=payload_image["sampler_index"],
            cfg_scale=payload_image["cfg_scale"],
            seed=payload_image["seed"],
            height=payload_image["height"],
            width=payload_image["width"],
            steps=payload_image["steps"],
            image_bytes=image_bytes,
        )
    
        
        return Response({
            "status": "success",
            "data": ollama_text.id,
        })
        
    
    @action(detail=False, methods=['get'])
    def invoke(self, request):
        # GET /api/v1/dev/invoke/
        
        MessageChannel.send("DEV - INVOKE")
        
        
        return Response({
            "status": "success",
            "data": "DEV - INVOKE"
        })
    
