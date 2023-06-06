module.exports = (sliceName) => `
import { rtkApi } from 'shared/api/rtkApi';

const ${sliceName}Api = rtkApi.injectEndpoints({
    endpoints: (build) => ({
        get${sliceName}: build.query<void, void>({
            query: () => ({
                url: '/',
            }),
        }),
    }),
});

export const { get${sliceName} } = ${sliceName}Api.endpoints;
`;
