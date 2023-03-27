import { createAsyncThunk, createSlice, PayloadAction } from '@reduxjs/toolkit';
import { ThunkConfig } from 'app/providers/StoreProvider';
import { HYDRATE } from 'next-redux-wrapper';

import { User, UserSchema } from '../types/user';

const initialState: UserSchema = {
    data: [],
};

export const userState = createSlice({
    name: 'userState',
    initialState,
    reducers: {
        initUser: (state, { payload }: PayloadAction<UserSchema>) => {
            state.data = payload.data;
        },
    },
    extraReducers: {
        [HYDRATE]: (state, action) => {
            console.log('HYDRATE', action.payload);
            return {
                ...state,
                ...action.payload.userState,
            };
        },
    },
});

export const { actions: userActions } = userState;
export const { reducer: userReducer } = userState;

export const fetchAllUsers = createAsyncThunk<User[], void, ThunkConfig<string>>(
    'userSlice/getAll',
    async (_, thunkApi) => {
        const {
            extra, dispatch, rejectWithValue,
        } = thunkApi;
        try {
            const response = await extra.api.get('https://jsonplaceholder.typicode.com/todos?_limit=5');
            dispatch(userActions.initUser({ data: response.data }));

            return response.data;
        } catch (error) {
            return rejectWithValue('error');
        }
    },
);
