# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:02:35 2023

@author: Timot
"""

from typing import Optional
import os
from google.api_core.client_options import ClientOptions
from google.cloud import documentai  # type: ignore


class Image_to_doc:
    
    def __init__(self, path):
      os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'insert json file path'
      self.path = path
        
    def process_document(self,
        project_id: str,
        location: str,
        processor_id: str,
        file_path: str,
        mime_type: str,
        field_mask: Optional[str] = None,
        processor_version_id: Optional[str] = None,
    ):
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.DocumentProcessorServiceClient(client_options=opts)
    
        if processor_version_id:
            # The full resource name of the processor version, e.g.:
            # `projects/{project_id}/locations/{location}/processors/{processor_id}/processorVersions/{processor_version_id}`
            name = client.processor_version_path(
                project_id, location, processor_id, processor_version_id
            )
        else:
            # The full resource name of the processor, e.g.:
            # `projects/{project_id}/locations/{location}/processors/{processor_id}`
            name = client.processor_path(project_id, location, processor_id)
    
        # Read the file into memory
        with open(file_path, "rb") as image:
            image_content = image.read()
    
        # Load binary data
        raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)
    
        # Configure the process request
        request = documentai.ProcessRequest(
            name=name, raw_document=raw_document, field_mask=field_mask
        )
    
        result = client.process_document(request=request)
    
        # For a full list of `Document` object attributes, reference this page:
        # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document
        document = result.document
    
        # Read the text recognition output from the processor
        print("The document contains the following text:")
        print(document.text)
        return document
    
    def __call__(self):
        self.process_document(    
        'insert project id',
        'us', # Format is "us" or "eu"
        'insert processor id', # Create processor before running sample
        r'C:\Users\Timot\Documents\Image-to-Data\Forms\DL-1.JPG',
        'image/jpeg',
        )

I2D = Image_to_doc(r"C:\Users\Timot\Documents\Image-to-Data\Forms\DL-1.JPG")
I2D()

