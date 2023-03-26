import type { AppProps } from 'next/app';
import { appWithTranslation } from 'next-i18next';
import { wrapper } from 'app/providers/StoreProvider';
import { StoreProvider } from 'app/providers/StoreProvider/ui/StoreProvider';

const MyApp = ({ Component, ...pageProps }: AppProps) => {
    const { store, props } = wrapper.useWrappedStore(pageProps);

    return (
        <StoreProvider initialStore={store}>
            <Component {...props.pageProps} />
        </StoreProvider>
    );
};

export default appWithTranslation(MyApp);
