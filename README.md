# Django E-commerce Backend (DRF-based)

#### project structure (summarized):

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontFamily": "Courier New, monospace",
    "background": "#f8f1e4",
    "primaryColor": "#ffe37f",
    "primaryTextColor": "#000000",
    "secondaryColor": "#ff7f7f",
    "tertiaryColor": "#d0d0d0",
    "edgeLabelBackground": "#ffffff",
    "lineColor": "#000000",
    "nodeBorder": "#000000",
    "clusterBorder": "#000000",
    "defaultLinkColor": "#000000"
  }
}}%%
graph TD
    A["ecommerce/ (project root)"]
    A --> B["ecommerce/ (settings)"]
    A --> C["users/ (user management)"]
    A --> D["products/ (product & inventory)"]
    A --> E["orders/ (order processing)"]
    A --> F["payments/ (payment handling)"]
    A --> G["core/ (shared utilities)"]
    A --> H["manage.py"]
```

## Command for starting development

#### Create a virtual environment
`python -m venv .venv`

#### Activate the virtualenv
- windows `.venv\Scripts\activate`
- mac [or] linux `source .venv\Scripts\activate`

#### Install the packages
`pip install -r requirements.txt`

`cd ecommerce`

#### Make db migrations and migrate
   - `python manage.py makemigrations`
   - `python manage.py migrate`

#### Run the app in 8000
`python manage.py runserver 8000`