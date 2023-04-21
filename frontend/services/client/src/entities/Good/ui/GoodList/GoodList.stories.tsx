import { ComponentStory, ComponentMeta } from '@storybook/react';
import { mockedListGoods } from '../../tests/good';
import { GoodList } from './GoodList';

export default {
    title: 'entities/Good/GoodList',
    component: GoodList,
} as ComponentMeta<typeof GoodList>;

const Template: ComponentStory<typeof GoodList> = (args) => <GoodList {...args} />;

export const Idle = Template.bind({});
Idle.args = {
    goods: mockedListGoods,
};
