import type { AppProps } from 'next/app';
import { appWithTranslation } from 'next-i18next';
import { wrapper } from 'app/providers/StoreProvider';
import { StoreProvider } from 'app/providers/StoreProvider/ui/StoreProvider';

interface PageProps {
    pageProps: {
        id: number;
    };
}

const MyApp = ({ Component, ...rest }: Omit<AppProps, 'pageProps'> & PageProps) => {
    const { store, props } = wrapper.useWrappedStore(rest);

    return (
        <StoreProvider initialStore={store}>
            <Component {...props.pageProps} />
        </StoreProvider>
    );
};

// MyApp.getInitialProps = wrapper.getInitialAppProps((store) => async (appCtx): Promise<PageProps> => {
//     const childrenGip = await App.getInitialProps(appCtx);
//     return {
//         pageProps: {
//             ...childrenGip.pageProps,
//         },
//     };
// });

export default appWithTranslation(MyApp);
