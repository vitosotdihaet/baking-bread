import {
    AnyAction,
    combineReducers,
    Reducer,
    ReducersMapObject,
} from '@reduxjs/toolkit';
import {
    ReducerManager,
    StateSchema,
    StateSchemaKey,
} from './StateSchema';

export function createReducerManager(initialReducers: ReducersMapObject<StateSchema>): ReducerManager {
    const reducers: ReducersMapObject<StateSchema> = { ...initialReducers };
    let combinedReducer = combineReducers(reducers);
    let keysToRemove: StateSchemaKey[] = [];

    return {
        getReducerMap: () => reducers,
        reduce: (state: StateSchema, action: AnyAction) => {
            if (keysToRemove.length > 0) {
                state = { ...state };
                keysToRemove.forEach((key) => {
                    // @ts-ignore
                    delete state[key];
                });
                keysToRemove = [];
            }

            return combinedReducer(state, action);
        },
        add: (key: StateSchemaKey, reducer: Reducer) => {
            if (!key || reducers[key]) {
                return;
            }

            // @ts-ignore
            reducers[key] = reducer;
            combinedReducer = combineReducers(reducers);
        },
        remove: (key: StateSchemaKey) => {
            if (!key || !reducers[key]) {
                return;
            }
            // @ts-ignore
            delete reducers[key];
            keysToRemove.push(key);
            combinedReducer = combineReducers(reducers);
        },
    };
}
