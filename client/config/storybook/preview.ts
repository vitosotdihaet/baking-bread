import type { Preview } from '@storybook/react';
import { withScreenshot } from 'storycap';

export const decorators = [withScreenshot];

const preview: Preview = {
    parameters: {
        actions: { argTypesRegex: '^on[A-Z].*' },
        controls: {
            matchers: {
                color: /(background|color)$/i,
                date: /Date$/,
            },
        },
        screenshot: {
            delay: 200,
            viewpor: 'Iphone 5',
        },
    },
};

export default preview;
