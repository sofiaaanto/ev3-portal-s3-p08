# ArchivaCloud P-08

Integrantes:
- Mauricio Catalán Medina
- Sofía González Pradenas

## Descripción

Portal web para subir, listar y eliminar archivos en Amazon S3.

## Tecnologías

- FastAPI
- React
- Vite
- AWS S3

## NPM AUDIT y PIP-AUDIT

Se ejecutaron pip-audit y npm audit para revisar dependencias.

El entorno virtual del proyecto contiene únicamente las dependencias declaradas en requirements.txt (FastAPI, Uvicorn, boto3, Pydantic y librerías asociadas).

Las vulnerabilidades reportadas inicialmente por pip-audit correspondían al entorno global de Python del equipo de desarrollo y no a las dependencias instaladas en el entorno virtual del proyecto.

C:\Users\Mauricio\Desktop\ev3-portal-s3-p08\backend>pip-audit
Found 67 known vulnerabilities in 9 packages
Name                  Version ID                  Fix Versions
--------------------- ------- ------------------- -------------------
django                5.2.6   PYSEC-2025-106      4.2.25,5.1.13,5.2.7
django                5.2.6   PYSEC-2025-107      4.2.26,5.1.14,5.2.8
django                5.2.6   PYSEC-2025-108      4.2.26,5.1.14,5.2.8
django                5.2.6   PYSEC-2025-104      4.2.27,5.1.15,5.2.9
django                5.2.6   PYSEC-2025-109      4.2.27,5.1.15,5.2.9
django                5.2.6   PYSEC-2026-42       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-44       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-47       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-46       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-45       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-43       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-48       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-49       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-53       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-52       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-51       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-50       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-55       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-54       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-50       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-43       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-42       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2025-107      4.2.26,5.1.14,5.2.8
django                5.2.6   PYSEC-2025-109      4.2.27,5.1.15,5.2.9
django                5.2.6   PYSEC-2026-44       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2025-108      4.2.26,5.1.14,5.2.8
django                5.2.6   PYSEC-2026-46       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2025-106      4.2.25,5.1.13,5.2.7
django                5.2.6   PYSEC-2026-45       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2025-104      4.2.27,5.1.15,5.2.9
django                5.2.6   PYSEC-2026-53       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-48       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-49       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-52       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-47       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-51       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-55       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-54       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-199      5.2.15,6.0.6
django                5.2.6   PYSEC-2026-197      5.2.15,6.0.6
django                5.2.6   PYSEC-2026-200      5.2.15,6.0.6
django                5.2.6   PYSEC-2026-198      5.2.15,6.0.6
django                5.2.6   PYSEC-2026-201      5.2.15,6.0.6
django                5.2.6   CVE-2025-59682      4.2.25,5.1.13,5.2.7
django                5.2.6   CVE-2026-25674      4.2.29,5.2.12,6.0.3
django                5.2.6   CVE-2026-25673      4.2.29,5.2.12,6.0.3
django-rest-framework 0.1.0   CVE-2018-25045      3.9.1
idna                  3.11    PYSEC-2026-215      3.15
pillow                11.3.0  PYSEC-2026-165      12.2.0
pillow                11.3.0  PYSEC-2026-165      12.2.0
pillow                11.3.0  CVE-2026-25990      12.1.1
pillow                11.3.0  CVE-2026-40192      12.2.0
pillow                11.3.0  CVE-2026-42309      12.2.0
pillow                11.3.0  CVE-2026-42310      12.2.0
pillow                11.3.0  CVE-2026-42311      12.2.0
pip                   25.2    PYSEC-2026-196      26.1.2
pip                   25.2    CVE-2025-8869       25.3
pip                   25.2    CVE-2026-1703       26.0
pip                   25.2    CVE-2026-3219       26.1
pip                   25.2    CVE-2026-6357       26.1
python-dotenv         1.2.1   CVE-2026-28684      1.2.2
requests              2.32.5  CVE-2026-25645      2.33.0
sqlparse              0.5.3   GHSA-27jp-wm6q-gp25 0.5.4
urllib3               2.5.0   PYSEC-2026-141      2.7.0
urllib3               2.5.0   CVE-2025-66418      2.6.0
urllib3               2.5.0   CVE-2025-66471      2.6.0
urllib3               2.5.0   CVE-2026-21441      2.6.3

C:\Users\Mauricio\Desktop\ev3-portal-s3-p08\backend>npm audit
found 0 vulnerabilities

C:\Users\Mauricio\Desktop\ev3-portal-s3-p08\backend>


C:\Users\Mauricio\Desktop\ev3-portal-s3-p08\frontend>npm audit
found 0 vulnerabilities

C:\Users\Mauricio\Desktop\ev3-portal-s3-p08\frontend>pip-audit
Found 67 known vulnerabilities in 9 packages
Name                  Version ID                  Fix Versions
--------------------- ------- ------------------- -------------------
django                5.2.6   PYSEC-2025-106      4.2.25,5.1.13,5.2.7
django                5.2.6   PYSEC-2025-107      4.2.26,5.1.14,5.2.8
django                5.2.6   PYSEC-2025-108      4.2.26,5.1.14,5.2.8
django                5.2.6   PYSEC-2025-104      4.2.27,5.1.15,5.2.9
django                5.2.6   PYSEC-2025-109      4.2.27,5.1.15,5.2.9
django                5.2.6   PYSEC-2026-42       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-44       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-47       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-46       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-45       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-43       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-48       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-49       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-53       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-52       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-51       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-50       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-55       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-54       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-50       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-43       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-42       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2025-107      4.2.26,5.1.14,5.2.8
django                5.2.6   PYSEC-2025-109      4.2.27,5.1.15,5.2.9
django                5.2.6   PYSEC-2026-44       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2025-108      4.2.26,5.1.14,5.2.8
django                5.2.6   PYSEC-2026-46       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2025-106      4.2.25,5.1.13,5.2.7
django                5.2.6   PYSEC-2026-45       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2025-104      4.2.27,5.1.15,5.2.9
django                5.2.6   PYSEC-2026-53       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-48       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-49       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-52       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-47       4.2.28,5.2.11,6.0.2
django                5.2.6   PYSEC-2026-51       4.2.30,5.2.13,6.0.4
django                5.2.6   PYSEC-2026-55       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-54       5.2.14,6.0.5
django                5.2.6   PYSEC-2026-199      5.2.15,6.0.6
django                5.2.6   PYSEC-2026-197      5.2.15,6.0.6
django                5.2.6   PYSEC-2026-200      5.2.15,6.0.6
django                5.2.6   PYSEC-2026-198      5.2.15,6.0.6
django                5.2.6   PYSEC-2026-201      5.2.15,6.0.6
django                5.2.6   CVE-2025-59682      4.2.25,5.1.13,5.2.7
django                5.2.6   CVE-2026-25674      4.2.29,5.2.12,6.0.3
django                5.2.6   CVE-2026-25673      4.2.29,5.2.12,6.0.3
django-rest-framework 0.1.0   CVE-2018-25045      3.9.1
idna                  3.11    PYSEC-2026-215      3.15
pillow                11.3.0  PYSEC-2026-165      12.2.0
pillow                11.3.0  PYSEC-2026-165      12.2.0
pillow                11.3.0  CVE-2026-25990      12.1.1
pillow                11.3.0  CVE-2026-40192      12.2.0
pillow                11.3.0  CVE-2026-42309      12.2.0
pillow                11.3.0  CVE-2026-42310      12.2.0
pillow                11.3.0  CVE-2026-42311      12.2.0
pip                   25.2    PYSEC-2026-196      26.1.2
pip                   25.2    CVE-2025-8869       25.3
pip                   25.2    CVE-2026-1703       26.0
pip                   25.2    CVE-2026-3219       26.1
pip                   25.2    CVE-2026-6357       26.1
python-dotenv         1.2.1   CVE-2026-28684      1.2.2
requests              2.32.5  CVE-2026-25645      2.33.0
sqlparse              0.5.3   GHSA-27jp-wm6q-gp25 0.5.4
urllib3               2.5.0   PYSEC-2026-141      2.7.0
urllib3               2.5.0   CVE-2025-66418      2.6.0
urllib3               2.5.0   CVE-2025-66471      2.6.0
urllib3               2.5.0   CVE-2026-21441      2.6.3

C:\Users\Mauricio\Desktop\ev3-portal-s3-p08\frontend>
