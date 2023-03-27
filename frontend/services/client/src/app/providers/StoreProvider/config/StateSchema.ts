import { AuthSchema, authState } from 'features/Auth';
import {
    Reducer,
    AnyAction,
    CombinedState,
    EnhancedStore,
    ReducersMapObject,
} from '@reduxjs/toolkit';
import { AxiosInstance } from 'axios';
import { userState } from 'features/UserList';
import { UserSchema } from 'features/UserList/model/types/user';

export interface StateSchema {
    [userState.name]: UserSchema;

    // async
    [authState.name]?: AuthSchema;
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
