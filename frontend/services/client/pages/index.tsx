import { serverSideTranslations } from 'next-i18next/serverSideTranslations';
import { wrapper } from 'app/providers/StoreProvider';
import HomePage from 'pages/HomePage';
import { getGoodsWithType } from 'widgets/Navbar';

export const getStaticProps = wrapper.getStaticProps(({ dispatch }) => async ({ locale }) => {
    await dispatch(getGoodsWithType.initiate());

    return {
        props: {
            ...(await serverSideTranslations(locale ?? 'en')),
        },
    };
});

export default HomePage;
