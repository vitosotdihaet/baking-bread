import { ComponentStory, ComponentMeta } from '@storybook/react';
import { GoodListWithType } from './GoodListWithType';

export default {
    title: 'features/GoodListWithType',
    component: GoodListWithType,
    argTypes: {
        backgroundColor: { control: 'color' },
    },
} as ComponentMeta<typeof GoodListWithType>;

const Template: ComponentStory<typeof GoodListWithType> = (args) => <GoodListWithType {...args} />;

export const Normal = Template.bind({});
Normal.args = {

};
