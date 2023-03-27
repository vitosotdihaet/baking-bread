import { ThunkConfig } from 'app/providers/StoreProvider';
import { createAsyncThunk } from '@reduxjs/toolkit';
import { AuthSchema } from '../../types/auth';

export interface LoginData {
    access_token?: string;
    refresh_token?: string;
}

export const loginByUsername = createAsyncThunk<LoginData, AuthSchema, ThunkConfig<string>>(
    'auth/loginByUsername',
    async (loginData, thunkApi) => {
        const { extra, dispatch, rejectWithValue } = thunkApi;
        try {
            const response = await extra.api.post<LoginData>(
                'https://a14c-178-178-81-2.eu.ngrok.io/api/login',
                loginData,
            );

            if (!response.data) {
                throw new Error();
            }

            return response.data;
        } catch (error) {
            console.log(error);
            return rejectWithValue('error');
        }
    },
);
