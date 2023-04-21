import { Decorator } from '@storybook/react';
import 'app/styles/index.scss';
import { i18n } from 'i18next';
import { I18nextProvider } from 'react-i18next';

export const I18nDecorator = (i18n: i18n): Decorator => (Story) => (
    <I18nextProvider i18n={i18n}>
        <Story />
    </I18nextProvider>
);
