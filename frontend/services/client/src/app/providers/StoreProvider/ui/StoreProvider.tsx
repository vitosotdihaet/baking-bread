import { ReducersMapObject } from '@reduxjs/toolkit';
import { FC, ReactNode } from 'react';
import { Provider } from 'react-redux';
import { StateSchema } from '../config/StateSchema';
import { AppStore, createReduxStore } from '../config/store';

interface StoreProviderProps {
    children: ReactNode;
    initialStore?: AppStore;
    initialState?: DeepPartial<StateSchema>;
    asyncReducers?: DeepPartial<ReducersMapObject<StateSchema>>;
}

export const StoreProvider: FC<StoreProviderProps> = (props) => {
    const {
        children,
        initialStore,
        initialState,
        asyncReducers,
    } = props;

    if (__PROJECT__ === 'storybook') {
        console.log(__PROJECT__);
        const store = createReduxStore(
            initialState as StateSchema,
            asyncReducers as ReducersMapObject<StateSchema>,
        );

        return (
            <Provider store={store}>
                {children}
            </Provider>
        );
    }

    if (!initialStore) {
        return null;
    }

    return (
        <Provider store={initialStore}>
            {children}
        </Provider>
    );
};
