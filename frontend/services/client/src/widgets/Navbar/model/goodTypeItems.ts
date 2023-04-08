import { GoodType } from 'entities/Good';

export const goodTypesItems: GoodType[] = [
    {
        id: 1,
        name: 'Sweet Pastries',
        order: 1,
        goodsCount: 0,
    },
    {
        id: 3,
        name: 'Breads',
        order: 3,
        goodsCount: 0,
    },
    {
        id: 4,
        name: 'Indulgent Bites',
        order: 4,
        goodsCount: 0,
    },
    {
        id: 2,
        name: 'Savory Pastries',
        order: 2,
        goodsCount: 0,
    },
].sort((a, b) => a.order - b.order);
