import { ComponentStory, ComponentMeta } from '@storybook/react';
import { Divider } from './Divider';

export default {
    title: 'shared/Divider',
    component: Divider,
    argTypes: {
        backgroundColor: { control: 'color' },
    },
} as ComponentMeta<typeof Divider>;

const Template: ComponentStory<typeof Divider> = (args) => <Divider {...args} />;

export const Normal = Template.bind({});
Normal.args = {

};
