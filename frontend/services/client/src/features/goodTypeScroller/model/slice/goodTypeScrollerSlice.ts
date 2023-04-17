import { PayloadAction, createSlice } from '@reduxjs/toolkit';

import { GoodTypeScrollerSchema } from '../types/GoodTypeScrollerSchema';

const initialState: GoodTypeScrollerSchema = {
    selectedType: '',
};

export const goodTypeScrollerSlice = createSlice({
    name: 'goodTypeScroller',
    initialState,
    reducers: {
        setSelectedType: (state, action: PayloadAction<string>) => {
            state.selectedType = action.payload;
        },
        initSelectedType: (state, action: PayloadAction<string>) => {
            state.selectedType = action.payload;
        },
    },
});

export const { actions: goodTypeScrollerActions } = goodTypeScrollerSlice;
export const { reducer: goodTypeScrollerReducer } = goodTypeScrollerSlice;
