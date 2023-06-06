import { ComponentStory, ComponentMeta } from '@storybook/react';
import { mockedListGoodType } from 'entities/Good/tests';
import { StoreDecorator } from 'shared/config/storybook/StoreDecorator';
import { GoodTypeScroller } from './GoodTypeScroller';

export default {
    title: 'features/GoodTypeScroller',
    component: GoodTypeScroller,
} as ComponentMeta<typeof GoodTypeScroller>;

const Template: ComponentStory<typeof GoodTypeScroller> = (args) => <GoodTypeScroller {...args} />;

export const Idle = Template.bind({});
Idle.args = {
    goodTypes: mockedListGoodType,
};
Idle.decorators = [StoreDecorator({
    goodTypeScroller: {
        selectedType: 'Savory Pastires',
    },
})];
