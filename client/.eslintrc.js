module.exports = {
    env: {
        browser: true,
        es2021: true,
        jest: true,
    },
    extends: [
        'airbnb',
        'eslint:recommended',
        'plugin:react/recommended',
        'plugin:@typescript-eslint/recommended',
        'plugin:i18next/recommended',
    ],
    parser: '@typescript-eslint/parser',
    parserOptions: {
        ecmaFeatures: {
            jsx: true,
        },
        ecmaVersion: 'latest',
        sourceType: 'module',
    },
    plugins: [
        'react',
        '@typescript-eslint',
        'i18next',
        'react-hooks',
    ],
    rules: {
        indent: ['error', 4],
        quotes: ['error', 'single'],
        semi: ['error', 'always'],
        'max-len': ['error', { ignoreComments: true, code: 110 }],
        'linebreak-style': 'off',
        'no-undef': 'off',
        'no-shadow': 'off',
        'react/jsx-indent': ['error', 4],
        'react/jsx-indent-props': ['error', 4],
        'react-hooks/rules-of-hooks': 'error',
        'react-hooks/exhaustive-deps': 'error',
        'react/react-in-jsx-scope': 'off',
        'react/jsx-filename-extension': [1, { extensions: ['.ts', '.tsx'] }],
        'react/function-component-definition': 'off',
        'react/require-default-props': 'off',
        'react/jsx-props-no-spreading': 'warn',
        'import/no-extraneous-dependencies': 'off',
        'import/prefer-default-export': 'off',
        'import/extensions': 'off',
        'import/no-unresolved': 'off',
        '@typescript-eslint/ban-ts-comment': 'warn',
        'i18next/no-literal-string': [
            'error',
            {
                markupOnly: true,
                ignoreAttribute: ['data-testid', 'to', 'theme', 'size', 'font', 'name'],
            },
        ],
    },
    overrides: [
        {
            files: ['**/src/**/*.{test,stories}.{ts,tsx}'],
            rules: {
                'i18next/no-literal-string': 'off',
                'max-len': 'off',
                'no-console': 'off',
            },
        },
        {
            files: ['next-i18next.config.js'],
            rules: {
                '@typescript-eslint/no-var-requires': 'off',
            },
        },
    ],
};
