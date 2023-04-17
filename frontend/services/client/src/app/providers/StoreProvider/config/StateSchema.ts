import {
    Reducer,
    AnyAction,
    CombinedState,
    EnhancedStore,
    ReducersMapObject,
} from '@reduxjs/toolkit';
import { AxiosInstance } from 'axios';
import { GoodTypeScrollerSchema, goodTypeScrollerSlice } from 'features/goodTypeScroller';
import { rtkApi } from 'shared/api/rtkApi';

export interface StateSchema {
    [rtkApi.reducerPath]: ReturnType<typeof rtkApi.reducer>;
    [goodTypeScrollerSlice.name]?: GoodTypeScrollerSchema;
}

export type StateSchemaKey = keyof StateSchema;

export interface ReducerManager {
    getReducerMap: () => ReducersMapObject<StateSchema>;
    reduce: (state: StateSchema, action: AnyAction) => CombinedState<StateSchema>;
    add: (key: StateSchemaKey, reducer: Reducer) => void;
    remove: (key: StateSchemaKey) => void;
}

export interface ReduxStoreWithManager extends EnhancedStore<StateSchema> {
    reducerManager: ReducerManager;
}

export interface ThunkExtraArg {
    api: AxiosInstance;
}

export interface ThunkConfig<T> {
    extra: ThunkExtraArg;
    rejectValue: T;
    state: StateSchema;
}
