import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { HYDRATE } from 'next-redux-wrapper';

export const rtkApi = createApi({
    reducerPath: 'api',
    baseQuery: fetchBaseQuery({
        baseUrl: 'https://eugenv.ru/api',
        prepareHeaders: (headers, api) => {
            headers.set('Access-Control-Allow-Origin', 'true');
            return headers;
        },
    }),
    extractRehydrationInfo: (action, { reducerPath }) => {
        if (action.type === HYDRATE) {
            return action.payload[reducerPath];
        }
    },
    endpoints: () => ({}),
    tagTypes: ['GoodTypes'],
});
