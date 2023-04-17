import {
    Action,
    CombinedState,
    configureStore,
    Reducer,
    ReducersMapObject,
    ThunkAction,
} from '@reduxjs/toolkit';
import { createWrapper } from 'next-redux-wrapper';
import { rtkApi } from 'shared/api/rtkApi';
import { createReducerManager } from './reducerManager';
import { StateSchema, ThunkExtraArg } from './StateSchema';

export const createReduxStore = (
    initialState?: StateSchema,
    asyncReducers?: ReducersMapObject<StateSchema>,
) => {
    const rootReducers: ReducersMapObject<StateSchema> = {
        ...asyncReducers,
        [rtkApi.reducerPath]: rtkApi.reducer,
    };

    const reducerManager = createReducerManager(rootReducers);

    const store = configureStore({
        reducer: reducerManager.reduce as Reducer<CombinedState<StateSchema>>,
        devTools: process.env.NODE_ENV === 'development',
        preloadedState: initialState,
        middleware: (getDefaultMiddleware) => getDefaultMiddleware({}).concat(rtkApi.middleware),
    });

    // @ts-ignore
    store.reducerManager = reducerManager;

    return store;
};

export type AppStore = ReturnType<typeof createReduxStore>;
export type AppState = ReturnType<AppStore['getState']>;
export type AppDispatch = AppStore['dispatch'];
export type AppThunk<ReturnType = void> = ThunkAction<ReturnType, AppState, ThunkExtraArg, Action>;

export const wrapper = createWrapper<AppStore>(
    // @ts-ignore
    createReduxStore,
    { debug: process.env.NODE_ENV === 'development' },
);
