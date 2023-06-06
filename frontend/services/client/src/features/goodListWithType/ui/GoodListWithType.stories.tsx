import { ComponentStory, ComponentMeta } from '@storybook/react';
import { mockedGoodType } from 'entities/Good/tests';
import { GoodListWithType } from './GoodListWithType';

export default {
    title: 'features/GoodListWithType',
    component: GoodListWithType,
} as ComponentMeta<typeof GoodListWithType>;

const Template: ComponentStory<typeof GoodListWithType> = (args) => <GoodListWithType {...args} />;

export const Idle = Template.bind({});
Idle.args = {
    goodType: mockedGoodType,
};
