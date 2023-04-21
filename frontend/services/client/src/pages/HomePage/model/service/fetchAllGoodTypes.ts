import { GoodType } from 'entities/Good';
import { rtkApi } from 'shared/api/rtkApi';

interface GoodTypeProps {
    name: string;
    description: string;
    order: number;
}

const goodTypesApi = rtkApi.injectEndpoints({
    endpoints: (build) => ({
        fetchGoodTypes: build.query<GoodType[], void>({
            query: () => ({
                url: '/good_types',
            }),
            transformResponse: (baseQuery: GoodType[]) => {
                return baseQuery.sort((a, b) => a.order - b.order);
            },
            providesTags: [{ type: 'GoodTypes' }],
        }),
        createGoodType: build.mutation<GoodType, GoodTypeProps>({
            query: (goodType) => ({
                url: '/good_types',
                method: 'POST',
                body: goodType,
            }),
            invalidatesTags: [{ type: 'GoodTypes' }],
        }),
        deleteAllGoodTypes: build.mutation<void, void>({
            query: () => ({
                url: '/good_types',
                method: 'DELETE',
            }),
            invalidatesTags: [{ type: 'GoodTypes' }],
        }),
    }),
});

export const {
    useFetchGoodTypesQuery,
    useCreateGoodTypeMutation,
    useDeleteAllGoodTypesMutation,
} = goodTypesApi;
export const { fetchGoodTypes } = goodTypesApi.endpoints;
