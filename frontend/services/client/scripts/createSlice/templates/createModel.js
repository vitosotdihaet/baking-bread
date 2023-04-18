const fs = require('fs/promises');
const resolveRoot = require('../resolveRoot');
const reduxSliceTemplate = require('./reduxSliceTemplate');
const schemaTypeTemplate = require('./schemaTypeTemplate');

module.exports = async (layer, sliceName) => {
    const resolveModelPath = (...segments) => resolveRoot('src', layer, sliceName, 'model', ...segments);

    const generateDirTemplate = async () => {
        try {
            await fs.mkdir(resolveModelPath());
            await fs.mkdir(resolveModelPath('types'));
            await fs.mkdir(resolveModelPath('slice'));
            await fs.mkdir(resolveModelPath('selectors'));
            await fs.mkdir(resolveModelPath('services'));
        } catch (error) {
            console.log('Model folders wasnt created.', error);
        }
    };

    const generateSliceTemplate = async () => {
        try {
            await fs.writeFile(
                resolveModelPath('slice', `${sliceName}.ts`),
                reduxSliceTemplate(sliceName),
            );
        } catch (error) {
            console.log('Slice wasnt created.', error);
        }
    };

    const generateSchemaTemplate = async () => {
        try {
            await fs.writeFile(
                resolveModelPath('types', `${sliceName}Schema`),
                schemaTypeTemplate(sliceName),
            );
        } catch (error) {
            console.log('Schema wasnt created', error);
        }
    };

    await generateDirTemplate();
    await generateSliceTemplate();
    await generateSchemaTemplate();
};
