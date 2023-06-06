import { ComponentStory, ComponentMeta } from '@storybook/react';
import { mockedGoodType } from 'entities/Good/tests/good';
import { GoodTypeItem } from './GoodTypeItem';

export default {
    title: 'entities/Good/GoodTypeItem',
    component: GoodTypeItem,
} as ComponentMeta<typeof GoodTypeItem>;

const Template: ComponentStory<typeof GoodTypeItem> = (args) => <GoodTypeItem {...args} />;

export const Idle = Template.bind({});
Idle.args = {
    goodType: mockedGoodType,
};
