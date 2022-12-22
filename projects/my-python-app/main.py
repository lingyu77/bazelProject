from flask import Flask
from random import randint
from flask_cors import CORS

from projects.calculator.calculator import Calculator

app = Flask(__name__)
CORS(app)
my_calculator = Calculator()


@app.route('/')
def hello():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    message = "{} + {} = {}".format(num1, num2, my_calculator.add(num1, num2))
    return message


@app.route('/v2/api-docs')
def apidocs():
    message = '''
openapi: 3.0.3
info:
  title: Risk Insights - Log Management Service
  description: |-
    The Risk-insights Log Management Service API is a RESTful API to allow you to retrieve, create, update, and delete objects with the HTTP verbs. The design of Risk-insights API speaks exclusively in JSON. Please set the content-type header to application/json to ensure the API accepts and processes your requests. Please refer to the page for the APIs are used by risk-insights team only.
  contact:
    email:  appliance-discovery@netskope.com
  version: 1.0.11
servers:
  - url: qalogmgmtsvchaproxy01.qa.local
  - url: stglogmgmtsvchaproxy01.stg.local
tags:
  - name: PII Privacy
    description: Protect certain fields for logs uploaded from appliance to Netskope Cloud.
  - name: Notification
    description: Configure emails for alerts.
paths:
  /piiprivacyconfig:
    put:
      tags:
        - PII Privacy
      summary: Create or replace (full update) a PII privacy configuration with a tenant id.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PiiPrivacy'
        required: true
      responses:
        '200':
          description: Successful operation
        '400':
          description: Bad Request
        '404':
          description: Not found
    get:
      tags:
        - PII Privacy
      summary: Get PII privacy configuration
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PiiPrivacyResponse'
        '400':
          description: Invalid status value
  /notification:
    get:
      tags:
        - Notification
      summary: Get email configuration
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Notification'
        '400':
          description: Invalid status value
    patch:
      tags:
        - Notification
      summary: Partially update a notification
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Notification'
      responses:
        '200':
          description: successful operation
        '400':
          description: Invalid status value
components:
  schemas:
    PiiPrivacy:
      required:
        - enabled
        - fields_to_protect
      type: object
      properties:
        enabled:
          type: boolean
          example: True
        fields_to_protect:
          type: object
    PiiPrivacyResponse:
      type: object
      properties:
        enabled:
          type: boolean
          example: True
        columns:
          type: array
          items:
            type: string
            example: domain
    Notification:
      type: object
      properties:
        emails:
          type: array
          items:
            type: string
            example: test@netskope.com

    '''
    return message


@app.route('/v2/api-docs/json')
def apidocsjson():
    message = '''
{
  "openapi": "3.0.0",
  "info": {
    "version": "1.0.0",
    "title": "Sample API",
    "description": "A sample API to illustrate OpenAPI concepts"
  },
  "paths": {
    "/list": {
      "get": {
        "description": "Returns a list of stuff",
        "responses": {
          "200": {
            "description": "Successful response"
          }
        }
      }
    }
  }
}
    '''
    return message

if __name__ == "__main__":
    app.run()
