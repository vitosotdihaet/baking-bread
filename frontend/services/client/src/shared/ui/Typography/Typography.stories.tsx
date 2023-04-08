import { ComponentStory, ComponentMeta } from '@storybook/react';
import { Typography } from './Typography';

export default {
    title: 'shared/Typography',
    component: Typography,
    argTypes: {
        backgroundColor: { control: 'color' },
    },
} as ComponentMeta<typeof Typography>;

const Template: ComponentStory<typeof Typography> = (args) => <Typography {...args} />;

export const Normal = Template.bind({});
Normal.args = {

};
