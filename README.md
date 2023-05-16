# FastAPI Vue.js PrimeVue Boilerplate

This is a boilerplate for FastAPI, Vue.js and PrimeVue.

<image src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="200" alt="FastAPI Logo" />

<image src="https://vuejs.org/images/logo.png" width="200" alt="Vue.js Logo" />

<image src="https://primefaces.org/cdn/primevue/images/primevue-logo-dark.svg" width="200" alt="PrimeVue Logo" />

# web

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

# api

## Create venv

```python
python -m venv .venv
```

## Active venv

```sh
.venv/Scripts/activate.sh
```
or
```PowerShell
.venv/Scripts/Activate.ps1
```

## Install requirements

```python
pip install -r requirements.txt
```

## Start server

```sh
uvicorn main:app --reload
```
