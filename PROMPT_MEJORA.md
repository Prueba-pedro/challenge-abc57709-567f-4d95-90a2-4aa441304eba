# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import datetime

# === ARCHIVO: app/main.py ===
app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# === ARCHIVO: app/models/transaction.py ===
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, index=True)

Base.metadata.create_all(bind=engine)

# === ARCHIVO: app/schemas/transaction.py ===
class TransactionCreate(BaseModel):
    amount: float
    status: str

class TransactionUpdate(BaseModel):
    amount: float = None
    status: str = None

class TransactionResponse(BaseModel):
    id: int
    amount: float
    date: datetime.datetime
    status: str

# === ARCHIVO: app/crud/transaction.py ===
def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def update_transaction(db: Session, transaction_id: int, transaction: TransactionUpdate):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    for key, value in transaction.dict(exclude_unset=True).items():
        setattr(db_transaction, key, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(db_transaction)
    db.commit()

# === ARCHIVO: app/api/transaction.py ===
@app.post("/transactions/", response_model=TransactionResponse)
def create_transaction_endpoint(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, transaction)

@app.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def get_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    transaction = get_transaction(db, transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.put("/transactions/{transaction_id}", response_model=TransactionResponse)
def update_transaction_endpoint(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    return update_transaction(db, transaction_id, transaction)

@app.delete("/transactions/{transaction_id}")
def delete_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    delete_transaction(db, transaction_id)
    return {"detail": "Transaction deleted"}

# === ARCHIVO: tests/test_transaction.py ===
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.models.transaction import Base, Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.crud.transaction import create_transaction, get_transaction, update_transaction, delete_transaction
from fastapi.testclient import TestClient

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_transaction():
    transaction = TransactionCreate(amount=100.0, status="pending")
    response = client.post("/transactions/", json=transaction.dict())
    assert response.status_code == 200
    assert response.json() == {"id": 1, "amount": 100.0, "date": response.json().get("date"), "status": "pending"}

def test_get_transaction():
    response = client.get("/transactions/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "amount": 100.0, "date": response.json().get("date"), "status": "pending"}

def test_update_transaction():
    transaction = TransactionUpdate(status="completed")
    response = client.put("/transactions/1", json=transaction.dict())
    assert response.status_code == 200
    assert response.json() == {"id": 1, "amount": 100.0, "date": response.json().get("date"), "status": "completed"}

def test_delete_transaction():
    response = client.delete("/transactions/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Transaction deleted"}

# === ARCHIVO: docs/openapi.yaml ===
openapi: 3.0.0
info:
  title: Transaction API
  version: 1.0.0
paths:
  /transactions/:
    post:
      summary: Create a new transaction
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TransactionCreate'
      responses:
        '200':
          description: Transaction created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TransactionResponse'
  /transactions/{transaction_id}:
    get:
      summary: Get a transaction by ID
      parameters:
        - name: transaction_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Transaction retrieved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TransactionResponse'
    put:
      summary: Update a transaction by ID
      parameters:
        - name: transaction_id
          in: path
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TransactionUpdate'
      responses:
        '200':
          description: Transaction updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TransactionResponse'
    delete:
      summary: Delete a transaction by ID
      parameters:
        - name: transaction_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Transaction deleted
          content:
            application/json:
              schema:
                type: object
                properties:
                  detail:
                    type: string
                    example: 'Transaction deleted'
components:
  schemas:
    TransactionCreate:
      type: object
      required:
        - amount
        - status
      properties:
        amount:
          type: number
          format: float
        status:
          type: string
    TransactionUpdate:
      type: object
      properties:
        amount:
          type: number
          format: float
        status:
          type: string
    TransactionResponse:
      type: object
      required:
        - id
        - amount
        - date
        - status
      properties:
        id:
          type: integer
        amount:
          type: number
          format: float
        date:
          type: string
          format: date-time
        status:
          type: string

```
