import { StateSchema } from 'app/providers/StoreProvider';

export const getLoginUsername = (state: StateSchema) => state.authState?.username || '';
export const getLoginPassword = (state: StateSchema) => state.authState?.password || '';
export const getLoginData = (state: StateSchema) => state.authState?.data || {};
