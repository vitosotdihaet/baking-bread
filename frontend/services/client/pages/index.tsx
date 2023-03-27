import { serverSideTranslations } from 'next-i18next/serverSideTranslations';
import { wrapper } from 'app/providers/StoreProvider';
import { fetchAllUsers } from 'features/UserList/model/slice/userSlice';
import HomePage from 'pages/HomePage/ui/HomePage';

export const getStaticProps = wrapper.getStaticProps(({ dispatch }) => async ({ locale }) => {
    await dispatch(fetchAllUsers());

    return {
        props: {
            ...(await serverSideTranslations(locale ?? 'en')),
        },
    };
});

export default HomePage;
