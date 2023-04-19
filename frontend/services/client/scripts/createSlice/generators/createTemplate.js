const fs = require('fs/promises');
const resolveRoot = require('../resolveRoot');
const createApi = require('./createApi');
const createModel = require('./createModel');
const createPublicApi = require('./createPublicApi');
const createUI = require('./createUI');

module.exports = async (layer, sliceName, args) => {
    const { model, api } = args;
    try {
        await fs.mkdir(resolveRoot('src', layer, sliceName));
    } catch (error) {
        console.log(`Не удалось создать директорию слайса ${sliceName}`);
    }

    if (model) await createModel(layer, sliceName);
    if (api) await createApi(layer, sliceName);

    await createUI(layer, sliceName);
    await createPublicApi(layer, sliceName);
};
