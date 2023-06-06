import { createSlice } from '@reduxjs/toolkit';

import { HYDRATE } from 'next-redux-wrapper';
import { GoodsSchema } from '../types/goods';

const initialState: GoodsSchema = {
    goodTypes: [],
};

export const goodsSlice = createSlice({
    name: 'goods',
    initialState,
    reducers: {
        setTypes: (state, action) => {
            state.goodTypes = action.payload;
        },
    },
    extraReducers: {
        [HYDRATE]: (state, action) => {
            console.log('HYDRATE', action.payload);
            return {
                ...state,
                ...action.payload.goods,
            };
        },
    },
});

export const { actions: goodsActions } = goodsSlice;
export const { reducer: goodsReducer } = goodsSlice;
