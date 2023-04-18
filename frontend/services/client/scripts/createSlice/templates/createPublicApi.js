const fs = require('fs/promises');
const firstCharUpperCase = require('../firstCharUpperCase');
const resolveRoot = require('../resolveRoot');

module.exports = async (layer, sliceName) => {
    const componentName = firstCharUpperCase(sliceName);
    const schemaName = `${sliceName}Schema`;

    try {
        await fs.writeFile(
            resolveRoot('src', layer, sliceName, 'index.ts'),
            `export { ${componentName} } from './ui/${componentName}/${componentName}'
             export { ${firstCharUpperCase} } from './model/types/${schemaName};'
            `,
        );
    } catch (error) {
        console.log('Public API in slice wasnt created.', error);
    }
};
