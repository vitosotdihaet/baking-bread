import { appWithTranslation } from 'next-i18next';
import { wrapper } from 'app/providers/StoreProvider';
import { StoreProvider } from 'app/providers/StoreProvider/ui/StoreProvider';
import type { AppProps } from 'next/app';
import 'src/app/styles/index.scss';

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

export default appWithTranslation(MyApp);
