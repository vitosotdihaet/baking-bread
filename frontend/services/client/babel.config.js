module.exports = {
    presets: [
        ['@babel/preset-env', { targets: { node: 'current' } }],
        'next/babel',
        '@babel/preset-typescript',
    ],
    plugins: ['inline-react-svg'],
};
