import { ReducersMapObject } from '@reduxjs/toolkit';
import { Decorator } from '@storybook/react';
import { StateSchema, StoreProvider } from 'app/providers/StoreProvider';
import { ReducersList } from '../../lib/components/DynamicModuleLoader/DynamicModuleLoader';

const defaultReducers: ReducersList = {
};

export const StoreDecorator = (
    state: DeepPartial<StateSchema>,
    asyncReducers?: DeepPartial<ReducersMapObject<StateSchema>>,
): Decorator => (Story) => {
    return (
        <StoreProvider initialState={state} asyncReducers={{ ...defaultReducers, ...asyncReducers }}>
            <Story />
        </StoreProvider>
    );
};
