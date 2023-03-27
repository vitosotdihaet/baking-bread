import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { loginByUsername, LoginData } from '../services/loginByUsername/loginByUsername';
import { AuthSchema } from '../types/auth';

const initialState: AuthSchema = {
    username: '',
    password: '',
    data: {},
};

export const authState = createSlice({
    name: 'authState',
    initialState,
    reducers: {
        setUsername: (state, action: PayloadAction<string>) => {
            state.username = action.payload;
        },
        setPassword: (state, action: PayloadAction<string>) => {
            state.password = action.payload;
        },
    },
    extraReducers: (builder) => {
        builder.addCase(loginByUsername.fulfilled, (state, action: PayloadAction<LoginData>) => {
            state.data = action.payload;
        });
    },
});

export const { actions: authActions } = authState;
export const { reducer: authReducer } = authState;
