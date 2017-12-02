import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.baseURL = '/api/v1/';

axios.interceptors.request.use((config) => {
    return config;
}, (error) => {
    alert(error);
    return Promise.reject(error);
});
axios.interceptors.response.use((response) => {
    return response;
}, (error) => {
    return Promise.reject(error.response);
});

global.axios = axios;