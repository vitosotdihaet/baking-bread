import axios from 'axios';

export const $api = axios.create({
    baseURL: process.env.API_URL,
});

$api.interceptors.request.use((config) => {
    const accessToken = localStorage.getItem('accessToken');

    config.headers.Authorization = `Bearer ${accessToken}`;
    return config;
});
