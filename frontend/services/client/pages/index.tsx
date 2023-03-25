import { HomePage } from 'pages/HomePage';
import { serverSideTranslations } from 'next-i18next/serverSideTranslations';

export async function getStaticProps({ locale }: any) {
    return {
        props: {
            ...(await serverSideTranslations(locale ?? 'en')),
        // Will be passed to the page component as props
        },
    };
}

export default HomePage;
