import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Set the REACT_APP_CODESPACE_URL from environment or fallback
const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
const protocol = window.location.protocol;
const port = '8000';
const host = codespaceName ? `${codespaceName}-8000.app.github.dev` : window.location.hostname;
const apiUrl = `${protocol}//${host}`;
process.env.REACT_APP_CODESPACE_URL = apiUrl;
console.log('REACT_APP_CODESPACE_URL:', apiUrl);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
