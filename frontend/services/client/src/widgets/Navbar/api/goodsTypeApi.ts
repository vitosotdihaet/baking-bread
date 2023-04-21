import { Good, GoodTypeWithGoods } from 'entities/Good';
import { rtkApi } from 'shared/api/rtkApi';

const goodsTypeApi = rtkApi.injectEndpoints({
    endpoints: (build) => ({
        getGoods: build.query<Good[], void>({
            query: () => ({
                url: '/good_types/goods',
            }),
        }),
        getGoodsWithType: build.query<GoodTypeWithGoods[], void>({
            query: () => ({
                url: '/good_types',
                params: {
                    expand: 'goods',
                },
            }),
        }),
    }),
});

export const { getGoodsWithType } = goodsTypeApi.endpoints;
export const useGetGoodsWithType = goodsTypeApi.useGetGoodsWithTypeQuery;
