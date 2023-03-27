import { FC, ReactNode } from 'react';
import { Provider } from 'react-redux';
import { AppStore } from '../config/store';

interface StoreProviderProps {
    children: ReactNode;
    initialStore: AppStore;
}

export const StoreProvider: FC<StoreProviderProps> = (props) => {
    const {
        children,
        initialStore,
    } = props;

    return (
        <Provider store={initialStore}>
            {children}
        </Provider>
    );
};
