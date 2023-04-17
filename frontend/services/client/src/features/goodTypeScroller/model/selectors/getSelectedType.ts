import { StateSchema } from 'app/providers/StoreProvider';

export const getSelectedType = (state: StateSchema) => state.goodTypeScroller?.selectedType || '';
